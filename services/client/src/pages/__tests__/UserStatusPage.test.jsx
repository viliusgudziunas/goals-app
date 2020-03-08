import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import UserStatusPage from '../UserStatusPage';

describe('<UserStatusPage />', () => {
  const wrapper = shallow(
    <Router location='/'>
      <UserStatusPage />
    </Router>
  );
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });
});

describe('When not authenticated, <UserStatusPage />', () => {
  const wrapper = shallow(<UserStatusPage />);
  it('should render a <NotAllowed />', () => {
    expect(wrapper.find('NotAllowed').length).toBe(1);
  });
});

// describe('When authenticated, <UserStatusPage />', () => {
//   const wrapper = shallow(<UserStatusPage />);
//   it('should render a <UserStatus />', () => {
//     expect(wrapper.find('UserStatus').length).toBe(1);
//   });
// });
