import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';

const users = [
  { id: 1, email: 'test@test.com', created_date: '2020-03-02T22:24:05.718728' },
  { id: 2, email: 'test2@test.com', created_date: '2020-03-02T22:24:05.718728' }
];

describe('<UsersList />', () => {
  const wrapper = shallow(<UsersList users={users} />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('should render 2 emails', () => {
    const list = wrapper.find('.list-group-item');
    expect(list.length).toBe(2);
    expect(list.get(0).props.children).toBe('test@test.com');
    expect(list.get(1).props.children).toBe('test2@test.com');
  });
});
