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
        element: <LoginPage />
      },
      {
        path: '/signup',
        element: <SignupPage />
      },
      {
        path: '/profile',
        element: <ProfilePage />
      },
      {
        path: '/shopping-cart',
        element: <ShoppingCartPage />
      },
      {
        path: '/products',
        element: <ProductsPage />
      },
      {
        path: '/create-product',
        element: <CreateProductPage />
      },
      {
        path: '/products/:productId',
        element: <ProductDetailPage />
      },
      {
        path: '/orders',
        element: <OrdersPage />
      }
    ]
  }
];

export default routes;
