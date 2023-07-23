import { FC } from 'react';
import { cn } from '@/utils';
import { NavLink } from 'react-router-dom';
import { useUserStore } from '@/hooks/stores/use-user-store.hook';

export const NavBar: FC = () => {
  const user = useUserStore((state) => state.user);

  return (
    <nav className={cn('flex justify-start space-x-4 m-6 lg:space-x-6')}>
      <NavLink
        to="/products"
        className={({ isActive }) =>
          cn(
            isActive
              ? 'text-primary'
              : 'text-muted-foreground transition-colors hover:text-primary/75',
            'text-lg font-medium'
          )
        }
      >
        Products
      </NavLink>
      <NavLink
        to="/orders"
        className={({ isActive }) =>
          cn(
            isActive
              ? 'text-primary'
              : 'text-muted-foreground transition-colors hover:text-primary/75',
            'text-lg font-medium'
          )
        }
      >
        Orders
      </NavLink>
      {!!user && (
        <NavLink
          to="/shopping-cart"
          className={({ isActive }) =>
            cn(
              isActive
                ? 'text-primary'
                : 'text-muted-foreground transition-colors hover:text-primary/75',
              'text-lg font-medium'
            )
          }
        >
          Shopping Cart
        </NavLink>
      )}
      {!!user && (
        <NavLink
          to="/create-product"
          className={({ isActive }) =>
            cn(
              isActive
                ? 'text-primary'
                : 'text-muted-foreground transition-colors hover:text-primary/75',
              'text-lg font-medium'
            )
          }
        >
          Create Product
        </NavLink>
      )}
      {!!user && (
        <NavLink
          to="/profile"
          className={({ isActive }) =>
            cn(
              isActive
                ? 'text-primary'
                : 'text-muted-foreground transition-colors hover:text-primary/75',
              'text-lg font-medium'
            )
          }
        >
          Profile
        </NavLink>
      )}
      {!user && (
        <NavLink
          to="/login"
          className={({ isActive }) =>
            cn(
              isActive
                ? 'text-primary'
                : 'text-muted-foreground transition-colors hover:text-primary/75',
              'text-lg font-medium'
            )
          }
        >
          Login
        </NavLink>
      )}
      {!user && (
        <NavLink
          to="/signup"
          className={({ isActive }) =>
            cn(
              isActive
                ? 'text-primary'
                : 'text-muted-foreground transition-colors hover:text-primary/75',
              'text-lg font-medium'
            )
          }
        >
          Signup
        </NavLink>
      )}
    </nav>
  );
};
