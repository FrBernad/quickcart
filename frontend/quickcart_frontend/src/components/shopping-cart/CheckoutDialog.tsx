import { Button } from '@/components/ui/button';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { useMutation } from '@tanstack/react-query';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { shoppingCartApi } from '@/services/shoppingCartApi';
import { toast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { Loader2 } from 'lucide-react';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form';

const checkoutSchema = z.object({
  card_number: z.string().nonempty('The card number is required'),
  expiration_year: z.number(),
  expiration_month: z.number(),
  cvv: z.number(),
  comments: z.string()
});

export function CheckoutDialog() {
  const form = useForm<z.infer<typeof checkoutSchema>>({
    resolver: zodResolver(checkoutSchema),
    defaultValues: {
      card_number: '',
      expiration_year: 0,
      expiration_month: 0,
      cvv: 0,
      comments: ' '
    }
  });

  const user = useUserStore((state) => state.user);

  const checkoutMutation = useMutation({
    mutationFn: async (checkoutData: z.infer<typeof checkoutSchema>) => {
      return await shoppingCartApi.checkout(user!.id!, checkoutData);
    },
    onSuccess() {
      toast({
        title: 'Products checked out!'
      });
    },
    onError({ response }: AxiosError<ResponseError>) {
      toast({
        variant: 'destructive',
        title: 'Uh oh! Something went wrong.',
        description: response?.data.message
      });
    }
  });
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button className="mt-4 inline-flex justify-center">Checkout</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Checkout Order</DialogTitle>
          <DialogDescription>
            Enter your payment details and checkout.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form
            onSubmit={form.handleSubmit(
              (checkoutData: z.infer<typeof checkoutSchema>) =>
                checkoutMutation.mutate(checkoutData)
            )}
            className="space-y-8"
          >
            <FormField
              control={form.control}
              name="card_number"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Card number</FormLabel>
                  <FormControl>
                    <Input
                      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="expiration_year"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Expiration year</FormLabel>
                  <FormControl>
                    <Input
                      type="number"
                      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="expiration_month"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Expiration month</FormLabel>
                  <FormControl>
                    <Input
                      type="number"
                      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="cvv"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>cvv</FormLabel>
                  <FormControl>
                    <Input
                      type="number"
                      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="comments"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Comments</FormLabel>
                  <FormControl>
                    <Input
                      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <DialogFooter>
              <Button
                className="mt-4 inline-flex justify-center"
                type="submit"
                disabled={checkoutMutation.isLoading}
              >
                Checkout
                {checkoutMutation.isLoading && (
                  <Loader2 className="ml-2 h-4 w-4 animate-spin" />
                )}
              </Button>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  );
}
