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
import { useNavigate } from 'react-router-dom';

const createProductSchema = z
  .object({
    name: z.string().nonempty('The email is required'),
    stock: z.number().gte(1, 'The stock must be greater than 0'),
    price: z.number().gte(1, 'The price must be greater than 0')
    // tags: z
    //   .array(z.string().nonempty('The tag must be non-empty'))
    //   .nonempty("The tags can't be empty")
  })
  .required();

export const CreateProductPage = () => {
  const form = useForm<z.infer<typeof createProductSchema>>({
    resolver: zodResolver(createProductSchema),
    defaultValues: {
      name: '',
      stock: 0,
      price: 0
      // tags: []
    }
  });

  // const navigate = useNavigate();

  const onSubmit = async (loginForm: z.infer<typeof createProductSchema>) => {
    console.log(loginForm);
    // navigate('/products/1');
  };

  const handleSubmit = () => {
    const stockStr = form.getValues('stock');
    const price = form.getValues('price');

    console.log(price);
    console.log(stockStr);

    form.handleSubmit(onSubmit);
  };

  // justify-content align-items
  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Create Product</h1>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Name</FormLabel>
                <FormControl>
                  <Input
                    placeholder="Product Name"
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
            name="price"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Price</FormLabel>
                <FormControl>
                  <Input
                    className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                    type="number"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="stock"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Stock</FormLabel>
                <FormControl>
                  <Input
                    className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"
                    type="number"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          {/*<label htmlFor="tags">Tags</label>*/}
          {/*{form.getValues().tags.map((tag, index) => (*/}
          {/*  <div key={index}>*/}
          {/*    <input*/}
          {/*      type="text"*/}
          {/*      value={tag}*/}
          {/*      onChange={(e) => handleTagChange(index, e.target.value)}*/}
          {/*    />*/}
          {/*    <button type="button" onClick={() => handleRemoveTag(index)}>*/}
          {/*      Remove*/}
          {/*    </button>*/}
          {/*  </div>*/}
          {/*))}*/}
          {/*<button type="button" onClick={handleAddTag}>*/}
          {/*  Add Tag*/}
          {/*</button>*/}
          {/*<FormItem>*/}
          {/*  <FormLabel>Tags</FormLabel>*/}
          {/*  <FormControl>*/}
          {/*    <Input*/}
          {/*      placeholder="Add a tag"*/}
          {/*      className="w-1/4 rounded border-2 border-gray-400/50 bg-transparent"*/}
          {/*    />*/}
          {/*  </FormControl>*/}
          {/*  <FormMessage />*/}
          {/*</FormItem>*/}
          <Button type="submit">Create</Button>
        </form>
      </Form>
    </div>
  );
};
