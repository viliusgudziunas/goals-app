export default (state, action) => {
  switch (action.type) {
    case 'AUTHENTICATE':
      return {
        ...state,
        authenticated: true
      };
    case 'LOGOUT':
      return {
        ...state,
        authenticated: false
      };
    default:
      return state;
  }
};
