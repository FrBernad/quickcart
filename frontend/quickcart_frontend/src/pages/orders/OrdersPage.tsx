import { useQuery } from '@tanstack/react-query';
import { HashLoader } from 'react-spinners';
import { OrderCard } from '@/components/orders/OrderCard';
import { ordersApi } from '@/services/ordersApi';

export const OrdersPage = () => {
  const { data: orders, isLoading } = useQuery({
    queryKey: [`orders`],
    queryFn: async ({ signal }) => {
      return await ordersApi.getUserOrders('user_id', signal!);
    }
  });

  // justify-content align-items
  return (
    <>
      <h1 className="mb-5 text-5xl font-bold">Orders</h1>

      <div className="flex flex-col gap-5">
        {!isLoading && !!orders && (
          <>
            <div className="grid grid-cols-4 gap-4">
              {orders.map((order) => (
                <OrderCard key={order.purchase_order_id} order={order} />
              ))}
            </div>
          </>
        )}
        {isLoading && (
          <div className="flex h-48 flex-row items-center justify-center">
            <HashLoader color="#36d7b7" />
          </div>
        )}
      </div>
    </>
  );
};
