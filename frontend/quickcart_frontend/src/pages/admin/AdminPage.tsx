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
import { useMutation } from '@tanstack/react-query';
import { Loader2 } from 'lucide-react';
import { ResponseError } from '@/models/ResponseError';
import { AxiosError } from 'axios';
import { toast } from '@/components/ui/use-toast';
import { categoriesApi } from '@/services/categoriesApi';

const createCategorySchema = z.object({
  name: z.string().nonempty('The category name is required')
});

export const AdminPage = () => {
  const form = useForm<z.infer<typeof createCategorySchema>>({
    resolver: zodResolver(createCategorySchema),
    defaultValues: {
      name: ''
    }
  });

  const createCategoryMutation = useMutation({
    mutationFn: async (
      createCategoryData: z.infer<typeof createCategorySchema>
    ) => {
      return await categoriesApi.createCategory(createCategoryData.name);
    },
    onSuccess() {
      toast({
        title: 'Category created!'
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

  // justify-content align-items
  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Create Category</h1>

      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(
            (createCategoryData: z.infer<typeof createCategorySchema>) =>
              createCategoryMutation.mutate(createCategoryData)
          )}
          className="space-y-8"
        >
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Category Name</FormLabel>
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
            disabled={createCategoryMutation.isLoading}
          >
            Create
            {createCategoryMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </Form>
    </div>
  );
};
