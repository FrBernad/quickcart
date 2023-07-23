import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { Product } from '@/models/Product';
import { Button } from '@/components/ui/button';

export const ShoppingCartPage = () => {
  const shoppingCart = useUserStore((state) => state.shoppingCart);
  const total = shoppingCart.reduce((acc, curr) => acc + curr.price, 0);
  // justify-content align-items
  return (
    <div>
      <h1 className="mb-5 text-5xl font-bold">Shopping Cart</h1>

      <h1 className="mb-5 text-4xl font-bold">Items</h1>
      {shoppingCart.map((product: Product) => (
        <p key={product.id}>
          {product.name} - {product.price} $
        </p>
      ))}
      {shoppingCart.length == 0 && (
        <p className="text-lg">Your shopping cart is empty</p>
      )}
      {shoppingCart.length > 0 && (
        <>
          <h2 className="mb-5 text-xl font-bold">Total: {total} $</h2>
          <Button className="mt-4" onClick={() => console.log('checkout')}>
            Checkout
          </Button>
        </>
      )}
    </div>
  );
};
