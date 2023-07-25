import { FC } from 'react';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import { Navigate } from 'react-router-dom';

interface Props {
  children: React.ReactNode;
}

export const AuthGuard: FC<Props> = ({ children }) => {
  const isAuthenticated = !!useUserStore((state) => state.user);
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};
