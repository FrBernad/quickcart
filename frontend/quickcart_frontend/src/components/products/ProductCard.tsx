import { Product } from '@/models/Product';
import { FC } from 'react';
import { Link } from 'react-router-dom';

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
            <span className="font-bold">Seller:</span> {product.seller}
          </p>
          <p>
            <span className="font-bold">Score:</span> {product.score}
          </p>
        </div>
      </div>
    </Link>
  );
};
