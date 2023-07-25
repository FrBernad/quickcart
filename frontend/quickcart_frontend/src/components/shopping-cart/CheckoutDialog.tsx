import { Button } from '@/components/ui/button';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { shoppingCartApi } from '@/services/shoppingCartApi';
import { toast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { Loader2 } from 'lucide-react';
import { useForm } from 'react-hook-form';
import { cn } from '@/utils';
import { ErrorField } from '@/components/forms/ErrorField';

export interface CheckoutFormInput {
  card_number: string;
  expiration_year: string;
  expiration_month: string;
  cvv: string;
  comments: string;
}

export function CheckoutDialog() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<CheckoutFormInput>();

  const user = useUserStore((state) => state.user);
  const queryClient = useQueryClient();

  const checkoutMutation = useMutation({
    mutationFn: async (checkoutData: CheckoutFormInput) => {
      return await shoppingCartApi.checkout(user!.id!, checkoutData);
    },
    onSuccess() {
      queryClient.invalidateQueries({
        queryKey: [`shoppingCart-${user!.id}`]
      });
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
        <form
          className={'m-8 space-y-4'}
          onSubmit={handleSubmit((formData) =>
            checkoutMutation.mutate(formData)
          )}
        >
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="card_number">Card Number</label>
            <Input
              id="card_number"
              {...register('card_number', { required: true })}
              className={cn('border-2')}
            />
            {errors.card_number && (
              <ErrorField error={'This field is required'} />
            )}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="expiration_month">Expiration Month</label>
            <Input
              id="expiration_month"
              type="number"
              {...register('expiration_month', {
                required: true
              })}
              className={cn('border-2')}
            />
            {errors.expiration_month && (
              <ErrorField error={'This field is required'} />
            )}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="expiration_year">Expiration Year</label>
            <Input
              id="expiration_year"
              type="number"
              {...register('expiration_year', {
                required: true
              })}
              className={cn('border-2')}
            />
            {errors.expiration_year && (
              <ErrorField error={'This field is required'} />
            )}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="cvv">CVV</label>
            <Input
              id="cvv"
              type="number"
              {...register('cvv', {
                required: true
              })}
              className={cn('border-2')}
            />
            {errors.cvv && <ErrorField error={'This field is required'} />}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="comments">Comments</label>
            <Input
              id="comments"
              type="string"
              {...register('comments', {
                required: true
              })}
              className={cn('border-2')}
            />
            {errors.comments && <ErrorField error={'This field is required'} />}
          </div>
          <Button
            className="mt-4 inline-flex justify-center rounded-md p-2"
            type="submit"
            disabled={checkoutMutation.isLoading}
          >
            Checkout
            {checkoutMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </DialogContent>
    </Dialog>
  );
}
