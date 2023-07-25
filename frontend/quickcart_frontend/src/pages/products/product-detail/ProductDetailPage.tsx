import { useParams } from 'react-router-dom';
import { FC } from 'react';
import { productsApi } from '@/services/productsApi';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Button } from '@/components/ui/button';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { shoppingCartApi } from '@/services/shoppingCartApi';
import { toast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { Loader2 } from 'lucide-react';

export const ProductDetailPage: FC = () => {
  const { productId } = useParams();

  const { data: product, isLoading } = useQuery({
    queryKey: [`product-${productId}`],
    queryFn: async ({ signal }) => {
      return await productsApi.getProductById(productId!, signal!);
    }
  });

  const user = useUserStore((state) => state.user);
  const queryClient = useQueryClient();

  const addProductMutation = useMutation({
    mutationFn: async () => {
      return await shoppingCartApi.addProduct(user!.id!, product!.id);
    },
    onSuccess() {
      toast({
        title: 'Product added to cart!'
      });
      queryClient.invalidateQueries({
        queryKey: [`shoppingCart-${user!.id}`]
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
    <>
      {!isLoading && !!product && (
        <div>
          <h1 className="mb-4 text-4xl font-bold">{product.name}</h1>
          <p>
            <span className="font-bold">Price:</span> {product.price}
          </p>
          <p>
            <span className="font-bold">Stock:</span> {product.stock}
          </p>
          <p>
            <span className="font-bold">Seller:</span> {product.owner.username}
          </p>
          <p>
            <span className="font-bold">Score:</span> {product.score}/5
          </p>
          {!!user && (
            <Button
              className="mt-4 inline-flex justify-center"
              onClick={() => addProductMutation.mutate()}
              disabled={addProductMutation.isLoading}
            >
              Add to Cart
              {addProductMutation.isLoading && (
                <Loader2 className="ml-2 h-4 w-4 animate-spin" />
              )}
            </Button>
          )}
        </div>
      )}
    </>
  );
};
