import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import UsersList from '../UsersList';

const users = [
  { id: 1, email: 'test@test.com', created_date: '2020-03-02T22:24:05.718728' },
  { id: 2, email: 'test2@test.com', created_date: '2020-03-02T22:24:05.718728' }
];

describe('UsersList', () => {
  it('renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users} />).toJSON();
    expect(tree).toMatchSnapshot();
  });

  const wrapper = shallow(<UsersList users={users} />);
  it('renders properly', () => {
    const element = wrapper.find('.list-group-item');

    expect(element.length).toBe(2);
    expect(element.get(0).props.children).toBe('test@test.com');
    expect(element.get(1).props.children).toBe('test2@test.com');
  });
});
