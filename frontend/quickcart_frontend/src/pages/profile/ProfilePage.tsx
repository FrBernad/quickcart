import { useUserStore } from '@/hooks/stores/use-user-store.hook';
import React from 'react';
import { Button } from '@/components/ui/button';
import { useNavigate } from 'react-router-dom';

export const ProfilePage = () => {
  const user = useUserStore((state) => state.user);
  const navigate = useNavigate();
  const logout = useUserStore((state) => state.logout);

  const logoutHandler = () => {
    logout();
    navigate('/login');
  };

  return (
    <>
      <h1 className="mb-5 text-5xl font-bold">Profile</h1>

      <h1 className="mb-5 text-2xl">
        <span className="font-bold">Email: </span>
        {user!.email}
      </h1>
      <h1 className="mb-5 text-2xl">
        <span className="font-bold">Username: </span>
        {user!.username}
      </h1>
      <Button className="mt-4" onClick={() => logoutHandler()}>
        Logout
      </Button>
    </>
  );
};
