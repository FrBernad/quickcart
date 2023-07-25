import { Button } from '@/components/ui/button';
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { toast } from '@/components/ui/use-toast';
import { AxiosError } from 'axios';
import { ResponseError } from '@/models/ResponseError';
import { Loader2 } from 'lucide-react';
import { useForm } from 'react-hook-form';
import { FC } from 'react';
import { reviewsApi } from '@/services/reviewsApi';
import { cn } from '@/utils';
import { ErrorField } from '@/components/forms/ErrorField';

interface Props {
  productId: number;
}

export interface CreateReviewFormInput {
  description: string;
  score: string;
}

export const ReviewDialog: FC<Props> = ({ productId }) => {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<CreateReviewFormInput>();

  const user = useUserStore((state) => state.user);
  const queryClient = useQueryClient();

  const createReviewMutation = useMutation({
    mutationFn: async ({
      description,
      score
    }: {
      description: string;
      score: string;
    }) => {
      return await reviewsApi.createReview(
        productId!,
        description,
        score,
        user!.id
      );
    },
    onSuccess() {
      toast({
        title: 'Review created!'
      });
      queryClient.invalidateQueries({
        queryKey: [`reviews-${productId!}`]
      });
      queryClient.invalidateQueries({
        queryKey: [`products-${productId!}`]
      });
    },
    onError({ response }: AxiosError<ResponseError>) {
      toast({
        variant: 'destructive',
        title: 'Uh oh! Something went wrong.',
        description: response?.data.message
      });
    }
  });

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button className="mt-4 inline-flex justify-center">
          Create review
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Create Review</DialogTitle>
        </DialogHeader>
        <form
          className={'m-8 space-y-4'}
          onSubmit={handleSubmit((formData) =>
            createReviewMutation.mutate(formData)
          )}
        >
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="description">Description</label>
            <Input
              id="description"
              {...register('description', { required: true })}
              className={cn('border-2')}
            />
            {errors.description && (
              <ErrorField error={'This field is required'} />
            )}
          </div>
          <div className={cn('flex flex-col space-y-1.5')}>
            <label htmlFor="score">Score</label>
            <Input
              id="score"
              type="number"
              {...register('score', { required: true, min: 0, max: 5 })}
              className={cn('border-2')}
            />
            {errors.score && <ErrorField error={'This field is required'} />}
          </div>
          <Button
            className="mt-4 inline-flex justify-center rounded-md p-2"
            type="submit"
            disabled={createReviewMutation.isLoading}
          >
            Create
            {createReviewMutation.isLoading && (
              <Loader2 className="ml-2 h-4 w-4 animate-spin" />
            )}
          </Button>
        </form>
      </DialogContent>
      <DialogFooter></DialogFooter>
    </Dialog>
  );
};
