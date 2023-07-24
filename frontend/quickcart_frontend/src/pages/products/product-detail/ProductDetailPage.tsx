import { useParams } from 'react-router-dom';
import { FC } from 'react';
import { productsApi } from '@/services/productsApi';
import { useQuery } from '@tanstack/react-query';
import { HashLoader } from 'react-spinners';
import { Button } from '@/components/ui/button';
import { Loader2 } from 'lucide-react';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';

export const ProductDetailPage: FC = () => {
  const { productId } = useParams();

  const { data: product, isFetching } = useQuery({
    queryKey: [`product-${productId}`],
    queryFn: async ({ signal }) => {
      return await productsApi.getProductById(productId!, signal!);
    }
  });

  const addProductToCart = useUserStore(
    (state) => state.addProductToShoppingCart
  );

  return (
    <>
      {!isFetching && !!product && (
        <div>
          <h1 className="text-4xl font-bold mb-4">{product.name}</h1>
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
          <Button className="mt-4" onClick={() => addProductToCart(product)}>
            {/*<Loader2 className="mr-2 h-4 w-4 animate-spin" />*/}
            Add to Cart
          </Button>
        </div>
      )}
      {/*{isFetching && (*/}
      {/*  <div className="flex h-48 flex-row items-center justify-center">*/}
      {/*    <HashLoader color="#36d7b7" />*/}
      {/*  </div>*/}
      {/*)}*/}
    </>
  );
};
