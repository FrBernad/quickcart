import { useForm } from 'react-hook-form';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { cn } from '@/utils';
import { useNavigate } from 'react-router-dom';
import { useMutation, useQuery } from '@tanstack/react-query';
import { productsApi } from '@/services/productsApi';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { toast } from '@/components/ui/use-toast';
import { ErrorField } from '@/components/forms/ErrorField';
import { categoriesApi } from '@/services/categoriesApi';
import Select from 'react-select';

export interface CreateProductFormInput {
  name: string;
  price: number;
  category_id: number;
  tags: string[];
  stock: number;
  user_id: number;
}

export const CreateProductPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<CreateProductFormInput>();

  const navigate = useNavigate();

  const { data: categories } = useQuery({
    queryKey: [`categories`],
    queryFn: async ({ signal }) => {
      return await categoriesApi.getCategories(signal!);
    },
    initialData: []
  });

  console.log(categories);

  const createProductMutation = useMutation({
    mutationFn: async (createProductData: CreateProductFormInput) => {
      return await productsApi.createProduct(createProductData);
    },
    onSuccess(product) {
      navigate(`/products/${product.id}`);
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
      <h1 className="mb-5 text-5xl font-bold">Create Product</h1>

      <div className={cn('m-2 grow container')}>
        <form
          className={'m-8 space-y-4'}
          onSubmit={handleSubmit((formData) =>
            createProductMutation.mutate(formData)
          )}
        >
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="name">Name</label>
            <Input
              id="name"
              {...register('name', { required: true })}
              className={cn('border-2')}
            />
            {errors.name && <ErrorField error={'This field is required'} />}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="price">Price</label>
            <Input
              id="price"
              type="number"
              {...register('price', { required: true })}
              className={cn('border-2')}
            />
            {errors.price && <ErrorField error={'This field is required'} />}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="stock">Stock</label>
            <Input
              id="stock"
              type="number"
              {...register('stock', { required: true })}
              className={cn('border-2')}
            />
            {errors.stock && <ErrorField error={'This is a required field'} />}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="stock">Stock</label>
            <Select options={categories.map((category) => category.name)} />
            {errors.category_id && (
              <ErrorField error={'This is a required field'} />
            )}
          </div>
          <Button type="submit" className={cn('rounded-md p-2')}>
            Create Product
          </Button>
        </form>
      </div>
    </div>
  );
};
