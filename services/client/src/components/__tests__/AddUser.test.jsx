import React from 'react';
import { shallow } from 'enzyme';

import AddUser from '../AddUser';

const pingFetchUsers = true;
const setPingFetchUsers = jest.fn();

describe('<AddUser />', () => {
  const wrapper = shallow(
    <AddUser
      pingFetchUsers={pingFetchUsers}
      setPingFetchUsers={setPingFetchUsers}
    />
  );
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  const form = wrapper.find('form');
  it('should have a form', () => {
    expect(form.length).toBe(1);
  });

  const formFields = form.find('input');
  it('should have one input field', () => {
    expect(formFields.length).toBe(1);
  });

  it('should have an email field', () => {
    expect(formFields.get(0).props.type).toBe('email');
  });

  it('should have a submit button', () => {
    expect(form.find('button').length).toBe(1);
    expect(form.find('button').get(0).props.type).toBe('submit');
  });
});
