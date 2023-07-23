import { Product } from '@/models/Product';
import { FC } from 'react';
import { Order } from '@/models/Order';

interface Props {
  order: Order;
}

export const OrderCard: FC<Props> = ({ order }) => {
  return (
    <div className="glass p-5">
      <h1 className="text-2xl font-bold">#{order.id}</h1>
      <div className="flex flex-col">
        {order.products.map((product: Product) => (
          <p key={product.id}>
            {product.name} - {product.price} $
          </p>
        ))}
        <p>
          <span className="font-bold">Total:</span> {order.total} $
        </p>
      </div>
    </div>
  );
};
