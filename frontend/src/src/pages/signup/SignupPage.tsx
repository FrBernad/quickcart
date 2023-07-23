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

const loginSchema = z.object({
  email: z.string().nonempty('The email is required'),
  password: z.string().nonempty('The password is required')
});

export const SignupPage = () => {
  const form = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: '',
      password: ''
    }
  });

  const navigate = useNavigate();

  const setUser = useUserStore((state) => state.setUser);

  const onSubmit = async (loginForm: z.infer<typeof loginSchema>) => {
    setUser({ email: loginForm.email, id: 1 });
    navigate('/products');
  };

  // justify-content align-items
  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Sign Up</h1>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
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
          <Button type="submit">Sign Up</Button>
        </form>
      </Form>
    </div>
  );
};
