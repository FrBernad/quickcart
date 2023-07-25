import { RootLayout } from '@/components/shared/RootLayout';
import { ErrorPage } from '@/pages/error/ErrorPage';
import { redirect, RouteObject } from 'react-router-dom';
import { ProductsPage } from '@/pages/products/ProductsPage';
import { OrdersPage } from '@/pages/orders/OrdersPage';
import { LoginPage } from '@/pages/login/LoginPage';
import { SignupPage } from '@/pages/signup/SignupPage';
import { ProductDetailPage } from '@/pages/products/product-detail/ProductDetailPage';
import { ProfilePage } from '@/pages/profile/ProfilePage';
import { ShoppingCartPage } from '@/pages/shopping-cart/ShoppingCartPage';
import { AdminPage } from '@/pages/admin/AdminPage';
import { AuthGuard } from '@/components/auth/AuthGuard';
import { UnauthGuard } from '@/components/auth/UnauthGuard';
import { CreateProductPage } from '@/pages/create-product/CreateProductPage';

const routes: RouteObject[] = [
  {
    path: '/',
    errorElement: <ErrorPage />,
    element: <RootLayout />,
    children: [
      {
        index: true,
        loader: async () => {
          return redirect(`/products`);
        }
      },
      {
        path: '/login',
        element: (
          <UnauthGuard>
            <LoginPage />
          </UnauthGuard>
        )
      },
      {
        path: '/signup',
        element: (
          <UnauthGuard>
            <SignupPage />
          </UnauthGuard>
        )
      },
      {
        path: '/profile',
        element: (
          <AuthGuard>
            <ProfilePage />
          </AuthGuard>
        )
      },
      {
        path: '/shopping-cart',
        element: (
          <AuthGuard>
            <ShoppingCartPage />
          </AuthGuard>
        )
      },
      {
        path: '/categories',
        element: (
          <AuthGuard>
            <AdminPage />
          </AuthGuard>
        )
      },
      {
        path: '/products',
        element: <ProductsPage />
      },
      {
        path: '/create-product',
        element: (
          <AuthGuard>
            <CreateProductPage />
          </AuthGuard>
        )
      },
      {
        path: '/admin',
        element: (
          <AuthGuard>
            <AdminPage />
          </AuthGuard>
        )
      },
      {
        path: '/products/:productId',
        element: <ProductDetailPage />
      },
      {
        path: '/orders',
        element: (
          <AuthGuard>
            <OrdersPage />
          </AuthGuard>
        )
      }
    ]
  }
];

export default routes;
