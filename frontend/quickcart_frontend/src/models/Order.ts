import { Product } from '@/models/Product';

export interface Order {
  id: number;
  products: Product[];
  total: number;
}
