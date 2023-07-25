import { cn } from '@/utils';

export const ErrorField = ({ error }: { error: string }) => {
  return <span className={cn('text-red-500 text-xs')}>{error}</span>;
};
