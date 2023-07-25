import { FC } from 'react';
import { Review } from '@/models/Review';

interface Props {
  review: Review;
}

export const ReviewCard: FC<Props> = ({ review }) => {
  return (
    <div className="flex flex-col">
      <div className="flex flex-row">
        <h1 className="text-2xl font-bold">{review.user.username}</h1>
        <p className="ml-2 text-2xl font-bold"> - {review.score}/5 ⭐</p>
      </div>
      <div>
        <p>{review.review_body}</p>
      </div>
    </div>
  );
};
