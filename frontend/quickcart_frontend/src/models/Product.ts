import { Tag } from '@/models/Tag';

export interface Category {
  id: number;
  name: string;
}

export interface Product {
  id: number;
  name: string;
  price: number;
  stock: number;
  score: number;
  tags: Tag[];
  owner: {
    username: string;
    id: number;
  };
  category: Category;
}
