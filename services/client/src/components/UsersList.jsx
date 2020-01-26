import React from 'react';

const UsersList = ({ users }) => {
  return (
    <div className="list-group list-group-flush">
      {users.map(user => {
        return (
          <div className="list-group-item" key={user.id}>
            {user.email}
          </div>
        );
      })}
    </div>
  );
};

export default UsersList;
