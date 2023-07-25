import { ProductCard } from '@/components/products/ProductCard';
import { useQuery } from '@tanstack/react-query';
import { HashLoader } from 'react-spinners';
import { productsApi } from '@/services/productsApi';

export const ProductsPage = () => {
  const { data: products, isLoading } = useQuery({
    queryKey: [`products`],
    queryFn: async ({ signal }) => {
      return await productsApi.getProducts(signal!);
    }
  });

  return (
    <>
      <h1 className="mb-5 text-5xl font-bold">Products</h1>
      <div className="flex flex-col gap-5">
        {!isLoading && !!products && (
          <>
            <div className="grid grid-cols-4 gap-4">
              {products.map((product) => (
                <ProductCard key={product.id} product={product} />
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
