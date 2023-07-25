import { useMutation, useQueryClient } from '@tanstack/react-query';
import { shoppingCartApi } from '@/services/shoppingCartApi';
import { toast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { Trash } from 'lucide-react';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { cn } from '@/utils';
import { ShoppingCartProduct } from '@/models/ShoppingCartProduct';

export function ShoppingCartProductCard({
  product
}: {
  product: ShoppingCartProduct;
}) {
  const user = useUserStore((state) => state.user);
  const queryClient = useQueryClient();

  const deleteFromProductCardMutation = useMutation({
    mutationFn: async () => {
      return await shoppingCartApi.removeProduct(user!.id, product.product_id);
    },
    onSuccess() {
      queryClient.invalidateQueries({
        queryKey: [`shoppingCart-${user!.id}`]
      });
      toast({
        title: 'Product deleted!'
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
    <div className="my-2 inline-flex">
      <p key={product.product_id}>
        {product.name} - {product.quantity}x{product.price} $ ={' '}
        {(product.price * product.quantity).toFixed(2)} $
      </p>
      <div
        className={cn('ml-2 cursor-pointer')}
        onClick={() => {
          if (deleteFromProductCardMutation.isLoading) return;
          deleteFromProductCardMutation.mutate();
        }}
      >
        <Trash
          color={deleteFromProductCardMutation.isLoading ? 'gray' : 'red'}
        />
      </div>
    </div>
  );
}
