import { User } from '@/models/User';

export interface Review {
  id: number;
  product_id: number;
  user_id: number;
  user: User;
  review_body: string;
}
