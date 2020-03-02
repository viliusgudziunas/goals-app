import React from 'react';
import PropTypes from 'prop-types';

const UsersList = ({ users }) => {
  return (
    <div className='list-group list-group-flush'>
      {users.map(user => {
        return (
          <div className='list-group-item' key={user.id}>
            {user.email}
          </div>
        );
      })}
    </div>
  );
};

UsersList.propTypes = {
  users: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      email: PropTypes.string.isRequired,
      created_date: PropTypes.string.isRequired
    }).isRequired
  ).isRequired
};

export default UsersList;
