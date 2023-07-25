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
import { usersApi } from '@/services/usersApi';
import { useMutation } from '@tanstack/react-query';
import React from 'react';
import { Loader2 } from 'lucide-react';
import { useToast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';

const loginSchema = z.object({
  email: z.string().nonempty('The email is required'),
  password: z.string().nonempty('The password is required')
});

export const LoginPage = () => {
  const form = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: '',
      password: ''
    }
  });

  const { toast } = useToast();

  const loginUpMutation = useMutation({
    mutationFn: async (signUpData: z.infer<typeof loginSchema>) => {
      return await usersApi.login(signUpData.email, signUpData.password);
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
      <h1 className="mb-5 text-5xl font-bold">Login</h1>

      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(
            (signUpData: z.infer<typeof loginSchema>) =>
              loginUpMutation.mutate(signUpData)
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
            disabled={loginUpMutation.isLoading}
          >
            Login
            {loginUpMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </Form>
    </div>
  );
};
