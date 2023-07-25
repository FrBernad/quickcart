import { Controller, useForm } from 'react-hook-form';
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
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { Loader2 } from 'lucide-react';

export interface CreateProductFormInput {
  name: string;
  price: string;
  category: { label: string; value: string };
  tags: string;
  stock: string;
}

export const CreateProductPage = () => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors }
  } = useForm<CreateProductFormInput>();

  const navigate = useNavigate();

  const user = useUserStore((state) => state.user);

  const { data: categories } = useQuery({
    queryKey: [`categories`],
    queryFn: async ({ signal }) => {
      return await categoriesApi.getCategories(signal!);
    },
    initialData: []
  });

  const categoriesOptions: ReadonlyArray<{
    value: string;
    label: string;
  }> =
    categories?.map((category) => ({
      value: category.id.toString(),
      label: category.name
    })) ?? [];

  const createProductMutation = useMutation({
    mutationFn: async (createProductData: CreateProductFormInput) => {
      return await productsApi.createProduct(user!.id, createProductData);
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

  const customStyles = {
    control: (styles: any) => ({
      ...styles,
      backgroundColor: 'transparent',
      borderColor: '#1E293B',
      borderWidth: '2px'
    }),
    menu: (styles: any) => ({
      ...styles,
      backgroundColor: 'white'
    }),
    option: (styles: any) => {
      return {
        ...styles,
        // backgroundColor:
        color: 'black'
      };
    },
    input: (styles: any) => ({ ...styles, color: 'white' }),
    placeholder: (styles: any) => ({ ...styles, color: 'white' }),
    singleValue: (provided: any) => ({
      ...provided,
      fontSize: '0.875rem',
      color: 'white'
    })
  };

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
            <label htmlFor="stock">Categoría</label>
            <Controller
              name="category"
              control={control}
              render={({ field }) => (
                <Select
                  {...field}
                  options={categoriesOptions}
                  styles={customStyles}
                />
              )}
            />
            {errors.category && (
              <ErrorField error={'This is a required field'} />
            )}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="stock">Tags</label>
            <Input
              id="tags"
              {...register('tags', { required: true })}
              className={cn('border-2')}
            />
            {errors.tags && <ErrorField error={'This is a required field'} />}
          </div>
          <Button
            type="submit"
            className="inline-flex justify-center rounded-md p-2"
            disabled={createProductMutation.isLoading}
          >
            Create Product
            {createProductMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </div>
    </div>
  );
};
