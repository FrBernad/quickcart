import { FC } from 'react';
import { cn } from '@/utils';

interface Props {
  tag: string;
}

export const ProductTagBadge: FC<Props> = ({ tag }) => {
  return (
    <span className="py-1 px-2 rounded text-xs font-medium text-white ring-1 ring-inset ring-gray-500/70">
      {tag}
    </span>
  );
};
