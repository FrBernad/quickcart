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
import { reviewsApi } from '@/services/reviewsApi';
import { ReviewCard } from '@/components/products/ReviewCard';
import { ReviewDialog } from '@/components/products/ReviewDialog';
import { ProductTagBadge } from '@/components/products/ProductTagBadge';

export const ProductDetailPage: FC = () => {
  const { productId: productIdStr } = useParams();
  const productId = parseInt(productIdStr!);

  const user = useUserStore((state) => state.user);

  const { data: product, isLoading: productIsLoading } = useQuery({
    queryKey: [`product-${productId!}`],
    queryFn: async ({ signal }) => {
      return await productsApi.getProductById(productId!, signal!);
    }
  });

  const { data: reviews, isLoading: reviewsIsLoading } = useQuery({
    queryKey: [`reviews-${productId!}`],
    queryFn: async ({ signal }) => {
      return await reviewsApi.getProductReviews(productId!, signal!);
    }
  });

  const queryClient = useQueryClient();

  const { data: shoppingCart } = useQuery({
    queryKey: [`shoppingCart-${user?.id}`],
    queryFn: async ({ signal }) => {
      return await shoppingCartApi.getShoppingCart(user!.id, signal!);
    },
    enabled: !!user
  });

  const addProductMutation = useMutation({
    mutationFn: async () => {
      let quantity = 1;
      shoppingCart?.forEach((product) => {
        if (product.product_id === productId) {
          quantity += product.quantity;
        }
      });
      return await shoppingCartApi.addProduct(user!.id!, product!.id, quantity);
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
      {!productIsLoading && !!product && (
        <div>
          <h1 className="mb-4 text-4xl font-bold">{product.name}</h1>
          <p>
            <span className="font-bold">Price:</span> {product.price} $
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
          <div className="mt-2 flex flex-row gap-2">
            {product.tags.map((tag) => (
              <ProductTagBadge key={tag.id} tag={tag.name} />
            ))}
          </div>
          {!!user && (
            <Button
              className="mr-2 mt-4 inline-flex justify-center"
              onClick={() => addProductMutation.mutate()}
              disabled={addProductMutation.isLoading}
            >
              Add to Cart
              {addProductMutation.isLoading && (
                <Loader2 className="ml-2 h-4 w-4 animate-spin" />
              )}
            </Button>
          )}
          {!!user && <ReviewDialog productId={product.id}></ReviewDialog>}
          <h1 className="my-4 text-4xl font-bold">Reviews</h1>
          {!reviewsIsLoading &&
            reviews!.length > 0 &&
            reviews!.map((review) => (
              <ReviewCard key={review.id} review={review}></ReviewCard>
            ))}
          {!reviewsIsLoading && reviews!.length === 0 && (
            <h1 className="text-2xl">No reviews yet</h1>
          )}
        </div>
      )}
    </>
  );
};
