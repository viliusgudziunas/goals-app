import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import AddUser from '../AddUser';

describe('AddUser', () => {
  it('renders a snapshot properly', () => {
    const tree = renderer.create(<AddUser />).toJSON();
    expect(tree).toMatchSnapshot();
  });

  const wrapper = shallow(<AddUser />);
  it('renders properly', () => {
    const form = wrapper.find('form');

    expect(form.find('input').length).toBe(1);
    expect(form.find('input').get(0).props.type).toBe('email');
    expect(form.find('button').get(0).props.type).toBe('submit');
  });
});
