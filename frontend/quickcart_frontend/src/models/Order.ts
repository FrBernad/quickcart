export interface Order {
  comments: string;
  products: {
    product_id: number;
    product_price: number;
    product_quantity: number;
    product_name: string;
  }[];
  purchase_order_id: 1;
  total_price: 20.4;
  user_id: 18;
}
