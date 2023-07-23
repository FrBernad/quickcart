import { useRouteError } from 'react-router-dom';
import { FC } from 'react';

export const ErrorPage: FC = () => {
  const error: any = useRouteError();

  return (
    <div className="m-6">
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      <p>
        <i>{error.statusText || error.message}</i>
      </p>
    </div>
  );
};
