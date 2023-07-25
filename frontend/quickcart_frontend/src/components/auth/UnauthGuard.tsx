import { FC } from 'react';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { Navigate } from 'react-router-dom';

interface Props {
  children: React.ReactNode;
}

export const UnauthGuard: FC<Props> = ({ children }) => {
  const isAuthenticated = !!useUserStore((state) => state.user);
  return isAuthenticated ? <Navigate to="/products" replace /> : children;
};
