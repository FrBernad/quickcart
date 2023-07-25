import { FC } from 'react';
import { Order } from '@/models/Order';
import { Link } from 'react-router-dom';

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
            <Link to={`/products/${product.product_id}`}>
              {product.product_name}
            </Link>{' '}
            - {product.product_quantity}x{product.product_price} $ ={' '}
            {(product.product_price * product.product_quantity).toFixed(2)} $
          </p>
        ))}
        <p>
          <span className="font-bold">Total:</span>{' '}
          {order.total_price.toFixed(2)} $
        </p>
      </div>
    </div>
  );
};
