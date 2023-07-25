import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { shoppingCartApi } from '@/services/shoppingCartApi';
import { useQuery } from '@tanstack/react-query';
import { HashLoader } from 'react-spinners';
import { CheckoutDialog } from '@/components/shopping-cart/CheckoutDialog';
import { ShoppingCartProductCard } from '@/components/shopping-cart/ShoppingCartProductCard';
import { ShoppingCartProduct } from '@/models/ShoppingCartProduct';

export const ShoppingCartPage = () => {
  const user = useUserStore((state) => state.user);
  const { data: shoppingCart, isLoading } = useQuery({
    queryKey: [`shoppingCart-${user!.id}`],
    queryFn: async ({ signal }) => {
      return await shoppingCartApi.getShoppingCart(user!.id, signal!);
    }
  });

  const total =
    shoppingCart
      ?.reduce((acc, curr) => acc + curr.price * curr.quantity, 0)
      .toFixed(2) ?? 0;

  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Shopping Cart</h1>
      {isLoading && (
        <div className="flex h-48 flex-row items-center justify-center">
          <HashLoader color="#36d7b7" />
        </div>
      )}

      {!isLoading && shoppingCart != undefined && (
        <div className="flex flex-col">
          <h1 className="mb-5 text-4xl font-bold">Items</h1>
          {shoppingCart.map((product: ShoppingCartProduct) => (
            <ShoppingCartProductCard
              key={product.product_id}
              product={product}
            />
          ))}
          {shoppingCart.length == 0 && (
            <p className="text-lg">Your shopping cart is empty</p>
          )}
          {shoppingCart.length > 0 && (
            <>
              <h2 className="mb-5 text-xl font-bold">Total: {total} $</h2>
              <div>
                <CheckoutDialog />
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};
