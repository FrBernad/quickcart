import { apiAxios } from '@/config/axiosConfig';
import { Review } from '@/models/Review';
import { usersApi } from '@/services/usersApi';

export const reviewsApi = {
  getProductReviews: async (
    productId: number,
    signal: AbortSignal
  ): Promise<Review[]> => {
    const response = await apiAxios.get<Review[]>(`/reviews`, {
      params: {
        product_id: productId
      },
      signal
    });
    if (response.status == 204) {
      return [];
    }

    for (const review of response.data) {
      review.user = await usersApi.getUserById(review.user_id, signal);
    }

    return response.data;
  },
  createReview: async (
    productId: number,
    description: string,
    score: string,
    userId: number
  ): Promise<void> => {
    await apiAxios.post<Review[]>(`/reviews/${productId}`, {
      description,
      score: parseInt(score),
      user_id: userId
    });
  }
};
