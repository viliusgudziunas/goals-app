import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import UsersList from '../UsersList';

const users = [
  { active: true, email: 'test@test.com', id: 1 },
  { active: true, email: 'test2@test.com', id: 2 }
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
