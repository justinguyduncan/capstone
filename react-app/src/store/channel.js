// Action Types
const SET_CHANNELS = 'channels/SET_CHANNELS';
const ADD_CHANNEL = 'channels/ADD_CHANNEL';
const UPDATE_CHANNEL = 'channels/UPDATE_CHANNEL';
const DELETE_CHANNEL = 'channels/DELETE_CHANNEL';


// Action Creators
const setChannels = (channels) => ({
    type: SET_CHANNELS,
    payload: channels,
  });

  const addChannel = (channel) => ({
    type: ADD_CHANNEL,
    payload: channel,
  });

  const updateChannel = (channel) => ({
    type: UPDATE_CHANNEL,
    payload: channel,
  });

  const deleteChannel = (channelId) => ({
    type: DELETE_CHANNEL,
    payload: channelId,
  });


  const initialState = {
    channels: [],
  };

  const channelsReducer = (state = initialState, action) => {
    switch (action.type) {
      case SET_CHANNELS:
        return {
          ...state,
          channels: action.payload,
        };
      case ADD_CHANNEL:
        return {
          ...state,
          channels: [...state.channels, action.payload],
        };
      case UPDATE_CHANNEL:
        return {
          ...state,
          channels: state.channels.map((channel) =>
            channel.id === action.payload.id ? action.payload : channel
          ),
        };
      case DELETE_CHANNEL:
        return {
          ...state,
          channels: state.channels.filter(
            (channel) => channel.id !== action.payload
          ),
        };
      default:
        return state;
    }
  };

  export default channelsReducer;
