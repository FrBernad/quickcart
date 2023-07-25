import { apiAxios } from '@/config/axiosConfig';
import { ShoppingCartProduct } from '@/models/ShoppingCartProduct';

export const shoppingCartApi = {
  getShoppingCart: async (
    userId: number,
    signal: AbortSignal
  ): Promise<ShoppingCartProduct[]> => {
    const response = await apiAxios.get<ShoppingCartProduct[]>(
      `/shopping-cart/${userId}`,
      {
        signal
      }
    );
    if (response.status === 204) return [];

    return response.data;
  },

  addProduct: async (
    userId: number,
    productId: number,
    quantity: number
  ): Promise<void> => {
    await apiAxios.put<void>(`/shopping-cart/${userId}/${productId}`, {
      quantity
    });
  },

  removeProduct: async (userId: number, productId: number): Promise<void> => {
    await apiAxios.delete<void>(`/shopping-cart/${userId}/${productId}`);
  },

  checkout: async (
    userId: number,
    checkoutData: {
      card_number: string;
      expiration_year: string;
      expiration_month: string;
      cvv: string;
      comments: string;
    }
  ): Promise<void> => {
    await apiAxios.post<void>(`/shopping-cart/${userId}/checkout`, {
      card_type: 'VISA',
      payment_method: 'CREDIT_CARD',
      card_number: checkoutData.card_number,
      expiration_year: parseInt(checkoutData.expiration_year),
      expiration_month: parseInt(checkoutData.expiration_month),
      cvv: checkoutData.cvv,
      comments: checkoutData.comments
    });
  }
};
