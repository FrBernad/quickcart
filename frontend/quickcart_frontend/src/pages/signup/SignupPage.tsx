import { useForm } from 'react-hook-form';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import * as z from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { Button } from '@/components/ui/button';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { useNavigate } from 'react-router-dom';
import { useMutation } from '@tanstack/react-query';
import { usersApi } from '@/services/usersApi';
import { Loader2 } from 'lucide-react';
import { ResponseError } from '@/models/ResponseError';
import { AxiosError } from 'axios';
import { toast } from '@/components/ui/use-toast';

const signUpSchema = z.object({
  email: z.string().nonempty('The email is required'),
  username: z.string().nonempty('The password is required'),
  password: z.string().nonempty('The password is required')
});

export const SignupPage = () => {
  const form = useForm<z.infer<typeof signUpSchema>>({
    resolver: zodResolver(signUpSchema),
    defaultValues: {
      email: '',
      username: '',
      password: ''
    }
  });

  const sigunUpMutation = useMutation({
    mutationFn: async (signUpData: z.infer<typeof signUpSchema>) => {
      return await usersApi.register(
        signUpData.email,
        signUpData.username,
        signUpData.password
      );
    },
    onSuccess(user) {
      useUserStore.getState().setUser(user);
      navigate('/products');
    },
    onError({ response }: AxiosError<ResponseError>) {
      toast({
        variant: 'destructive',
        title: 'Uh oh! Something went wrong.',
        description: response?.data.message
      });
    }
  });

  const navigate = useNavigate();

  // justify-content align-items
  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Sign Up</h1>

      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(
            (signUpData: z.infer<typeof signUpSchema>) =>
              sigunUpMutation.mutate(signUpData)
          )}
          className="space-y-8"
        >
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Email</FormLabel>
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
            name="username"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Username</FormLabel>
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
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Password</FormLabel>
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
          <Button
            type="submit"
            className="inline-flex justify-center"
            disabled={sigunUpMutation.isLoading}
          >
            Sign Up
            {sigunUpMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </Form>
    </div>
  );
};
