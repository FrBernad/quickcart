import { create } from 'zustand';
import { User } from '@/models/User';
import { Product } from '@/models/Product';

interface userState {
  user?: User;
  shoppingCart: Product[];
}

interface userActions {
  setUser: (user: User) => void;
  addProductToShoppingCart: (product: Product) => void;
  logout: () => void;
}

const initialState: userState = {
  user: undefined,
  shoppingCart: []
};

export const useUserStore = create<userState & userActions>()((setState) => ({
  ...initialState,
  setUser: (user: User) => {
    setState((state) => {
      state.user = user;
      return {
        user: state.user
      };
    });
  },
  addProductToShoppingCart: (product: Product) => {
    setState((state) => {
      state.shoppingCart.push(product);
      return {
        shoppingCart: state.shoppingCart
      };
    });
  },
  logout: () => {
    setState(initialState);
  }
}));
