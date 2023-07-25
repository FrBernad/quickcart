import { apiAxios } from '@/config/axiosConfig';
import { Product } from '@/models/Product';

export const shoppingCartApi = {
  getShoppingCart: async (
    userId: number,
    signal: AbortSignal
  ): Promise<Product[]> => {
    const response = await apiAxios.get<Product[]>(`/shopping-cart/${userId}`, {
      signal
    });
    if (response.status === 204) return [];

    return response.data;
  },

  addProduct: async (userId: number, productId: number): Promise<void> => {
    await apiAxios.put<void>(`/shopping-cart/${userId}/${productId}`, {
      quantity: 1
    });
  },

  removeProduct: async (userId: number, productId: number): Promise<void> => {
    await apiAxios.delete<void>(`/shopping-cart/${userId}/${productId}`);
  },

  checkout: async (
    userId: number,
    checkoutData: {
      card_number: string;
      expiration_year: number;
      expiration_month: number;
      cvv: number;
      comments: string;
    }
  ): Promise<void> => {
    await apiAxios.post<void>(`/shopping-cart/${userId}/checkout`, {
      card_type: 'VISA',
      payment_method: 'CREDIT_CARD',
      ...checkoutData
    });
  }
};
