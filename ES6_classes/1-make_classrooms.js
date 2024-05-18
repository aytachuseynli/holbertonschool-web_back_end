/* eslint-disable no-unused-vars */
// eslint-disable-next-line import/extensions
import ClassRoom from './0-classroom';

function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34)
  ];
}

export default initializeRooms;