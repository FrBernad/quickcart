import { FC } from 'react';
import { Order } from '@/models/Order';

interface Props {
  order: Order;
}

export const OrderCard: FC<Props> = ({ order }) => {
  return (
    <div className="glass p-5">
      <h1 className="text-2xl font-bold">Order #{order.purchase_order_id}</h1>
      <div className="flex flex-col">
        {order.products.map((product) => (
          <p key={product.product_id}>
            {product.product_name} - {product.product_price} $
          </p>
        ))}
        <p>
          <span className="font-bold">Total:</span> {order.total_price} $
        </p>
      </div>
    </div>
  );
};
