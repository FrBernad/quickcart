import { FC } from 'react';
import { Review } from '@/models/Review';

interface Props {
  review: Review;
}

export const ReviewCard: FC<Props> = ({ review }) => {
  return (
    <div className="">
      <h1 className="text-2xl font-bold">{review.user.username}</h1>
      <div className="flex flex-col">
        <p>{review.review_body}</p>
      </div>
    </div>
  );
};
