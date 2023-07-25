import { create } from 'zustand';
import { User } from '@/models/User';

interface userState {
  user?: User;
}

interface userActions {
  setUser: (user: User) => void;
  logout: () => void;
}

const initialState: userState = {
  user: undefined
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
  logout: () => {
    setState(initialState);
  }
}));
