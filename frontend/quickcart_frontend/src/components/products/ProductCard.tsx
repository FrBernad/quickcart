import { Product } from '@/models/Product';
import { FC } from 'react';
import { Link } from 'react-router-dom';
import { ProductTagBadge } from '@/components/products/ProductTagBadge';

interface Props {
  product: Product;
}

export const ProductCard: FC<Props> = ({ product }) => {
  return (
    <Link to={`/products/${product.id}`}>
      <div className="glass p-5">
        <h1 className="text-2xl font-bold">{product.name}</h1>
        <div className="flex flex-col">
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
            <span className="font-bold">Score:</span> {product.score}
          </p>
          <div className="mt-2 flex flex-row gap-2">
            {product.tags.map((tag) => (
              <ProductTagBadge key={tag.id} tag={tag.name} />
            ))}
          </div>
        </div>
      </div>
    </Link>
  );
};
